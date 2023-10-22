import pika
    
#establish the RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#The queue for the first and second MQ is decleared
channel.queue_declare(queue='second_mq')
channel.queue_declare(queue='third_mq')

#split csv data and send to the third message queue
def split(ch, method, properties, body):
    rows_csv = body.decode("utf-8").split("\n")
    
    for i, part in enumerate(rows_csv):
        channel.basic_publish(exchange="", routing_key="third_mq", body=part)
    print("File sent!")


#Get the data from the second message queue
channel.basic_consume(queue="second_mq", on_message_callback=split, auto_ack=True)

print("Waiting... press ctrl+c to exit")
channel.start_consuming()