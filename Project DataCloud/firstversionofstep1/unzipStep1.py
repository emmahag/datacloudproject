import zipfile
import pika

#Unzip the needed files
with zipfile.ZipFile("mockZip.zip", "r") as zipped_file:
    zipped_file.extractall("mock_folder")
    
#establish the RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#The queue for the first MQ is decleared
channel.queue_declare(queue='first_mq')

#Get the data
unzipped_files = open("mock_folder/mockZip/mock.tsv", "r").read()

#Send the data to the first message queue
channel.basic_publish(exchange='', routing_key='first_mq', body=unzipped_files)
print("File sent!")

#Close connection
connection.close()