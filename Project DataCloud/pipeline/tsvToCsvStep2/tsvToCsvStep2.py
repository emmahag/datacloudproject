import pika
    
#establish the RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#The queue for the first and second MQ is decleared
channel.queue_declare(queue='first_mq')
channel.queue_declare(queue='second_mq')

#convert from tsv to csv and send to the second message queue
def convert(ch, method, properties, body): 
    data_csv = []
    for row in body.split("\n"):
        data_csv.append(row.split("\t"))
        
    data_csv_string = '\n'.join([','.join(row) for row in data_csv])
    
    channel.basic_publish(exchange="", routing_key="second_mq", body=data_csv_string)
    print("File sent!")
    

#Get the data from the first message queue
channel.basic_consume(queue="first_mq", on_message_callback=convert, auto_ack=True)

print("Waiting... press ctrl+c to exit")
channel.start_consuming()