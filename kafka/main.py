from confluent_kafka import Producer

producer = Producer(bootstrap_servers='localhost:9092', acks='all')
for _ in range(100):
    producer.send('foobar', b'some_message_bytes')

print("sending all messages to kafka")
print(f"sending all messages to kafka")
producer.flush()