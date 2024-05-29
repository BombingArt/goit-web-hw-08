import pika
from faker import Faker
from models import Contact


def generate_contacts(n):
    fake = Faker()
    contacts = []
    for _ in range(n):
        contact = Contact(full_name=fake.name(), email=fake.email())
        contact.save()
        contacts.append(contact)
    return contacts


def send_to_queue(contacts):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="email_queue")

    for contact in contacts:
        channel.basic_publish(
            exchange="", routing_key="email_queue", body=str(contact.id)
        )
        print(f" [x] Sent {contact.id}")

    connection.close()


if __name__ == "__main__":
    n = 5  # кількість контактів для генерації
    contacts = generate_contacts(n)
    send_to_queue(contacts)
