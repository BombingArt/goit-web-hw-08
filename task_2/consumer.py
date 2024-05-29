import pika
from models import Contact
from time import sleep


def send_email_stub(contact):
    print(f"Sending email to {contact.email}")
    sleep(1)
    print(f"Email sent to {contact.email}")


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()

    if contact and not contact.is_sent:
        send_email_stub(contact)
        contact.is_sent = True
        contact.save()
        print(f"Updated contact {contact.id} as sent.")
    else:
        print(f"Contact {contact_id} already processed or not found.")

    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="email_queue")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="email_queue", on_message_callback=callback)

    try:
        print(" [*] Connected to RabbitMQ successfully.")
        print(" [*] Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Interrupted")
    finally:
        try:
            if connection.is_open:
                connection.close()
        except Exception as e:
            print(f"Error closing connection: {e}")


if __name__ == "__main__":
    start_consumer()
