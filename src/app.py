from fastapi_offline import FastAPIOffline

app=FastAPIOffline()
mylist=[200,100,200,300]
@app.get('/')

def say_hello():
    return{'HELLO':'WORLD'}


@app.get('/getItems/')
def get_item():
    return {'output':mylist}


@app.get('/lastItem/')
def get_last_item():
    if len(mylist)>0:
     return{'output':mylist[-1]}
    else:
       return{'list is Empty'}

@app.post('/AddItem/{new_item}')
def insert_item(new_item:int):
    mylist.append(new_item)
    return {'new output':mylist}


@app.delete('/RemoveItem/')
def remove_item(item:int):
   if item in mylist:
      mylist.remove(item)
      return{"list after remove":mylist}
   else:
      return{f'{item}Not Found in list'}


@app.delete('/PopIndex/')
def pop_item(index:int):
   if index >=0 and index <len(mylist):
      r=mylist.pop(index)
      return{f"{r} deleted from list"}
   else:
      return{'index is wrong'}
      

@app.put('/updateItem/')
def update_item(index:int,new_item:int):
   if index>=0 and index<len(mylist):
      mylist[index]=new_item
      return{'update list':mylist}
   else:
      return{f'index of {index},not exist in my list'}


app.put('/updateOldItem/')
def update_old_item(old_item:int,new_item:int):
   if old_item in mylist:
      i=mylist.index(old_item)
      mylist[i]=new_item
      return{'list update':mylist}
   else:
      return {f'{old_item}not found in my list'}
   
   