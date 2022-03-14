##                          TASK 5
##dict1 = {
## "april_batch":{
## "student":{
## "name":"Mike",
## "marks":{
## "python":80,
## "maths":70
## }
## }
## }
##}
##From the above dictionary, do the following tasks
##1. access "Mike"
##2. access 80
##3. change "Mike" to "Your name"
##4. add ML = 80 and DL = 80 inside mark

dict1 = {
 "april_batch":{
 "student":{
 "name":"Mike",
 "marks":{
 "python":80,
 "maths":70
 }
 }
 }
}
##1 - Access mike:
print(dict1["april_batch"]["student"]["name"])
##2 - Access 80
print(dict1["april_batch"]["student"]["marks"]["python"])
##3 - change "mike" to "Your name"
dict1["april_batch"]["student"]["name"]= "Your_name"
print(dict1["april_batch"]["student"]["name"])
##4 - add ML = 80 and Dl = 80 inside mark
dict1["april_batch"]["student"]["marks"]["ML"]=80
dict1["april_batch"]["student"]["marks"]["DL"]=80
print(dict1["april_batch"]["student"]["marks"])



