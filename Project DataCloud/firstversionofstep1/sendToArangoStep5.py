import pika
    
#establish the RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#The queue for the fourth MQ is declared
channel.queue_declare(queue='fourth_mq')

#function to send the data to Arango
def sendToArango(ch, method, properties, body):
    data = body.decode("utf-8")
    
    print(data)
    #if Arango was accessed
    #arango_client.db('my_database').collection('my_collection').insert(data)
    
#Get the data from the second message queue
channel.basic_consume(queue="fourth_mq", on_message_callback=sendToArango, auto_ack=True)

print("Waiting... press ctrl+c to exit")
channel.start_consuming()