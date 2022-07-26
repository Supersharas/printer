


function print(){
	var name = document.getElementById('name').value;
	var reference = document.getElementById('reference').value;
	var chequeNo = document.getElementById('chequeNumber').value;
	var amount = document.getElementById('amount').value;
	let msg = {"name": name,"reference": reference, "chequeNo": chequeNo, "amount": amount}

  console.log(msg)

	fetchPost("/go", msg).then(function(res){
		console.log(res);
	})
}

console.log('book', book)



function fetchPost(address, message){
  return fetch(address,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: JSON.stringify(message)
  }).then(response => response.json()).then(function(response){
    if(response['success'] == true){
      document.location.relode()
    }
    return response;
  }).catch(function(error){
  	console.log(error);
  })
}