from confluent_kafka import Producer

config = {'bootstrap.servers': 'localhost:9092'}

producer = Producer(config)
for _ in range(100):
    producer.produce('created_events', b'some_message_bytes')

print("sending all messages to kafka")
print(f"sending all messages to kafka")
producer.flush()