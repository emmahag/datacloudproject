import pika
    
#establish the RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#The queue for the first and second MQ is decleared
channel.queue_declare(queue='third_mq')
channel.queue_declare(queue='fourth_mq')

#split csv data and send to the third message queue
def grafterize(ch, method, properties, body):
    data = body.decode("utf-8")
    
    cleaned_data = data.lowercase() #dummy for Grafterize
    
    channel.basic_publish(exchange="", routing_key="fourth_mq", body=cleaned_data)


#Get the data from the second message queue
channel.basic_consume(queue="third_mq", on_message_callback=grafterize, auto_ack=True)

print("Waiting... press ctrl+c to exit")
channel.start_consuming()