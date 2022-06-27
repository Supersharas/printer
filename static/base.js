


function print(){
	var name = document.getElementById('name');
	var reference = document.getElementById('reference')
	var chequeNo = document.getElementById('chequeNumber')
	var amount = document.getElementById('amount')
	let msg = {"name": name,"reference": reference, chequeNo: "chequeNo", "amount": amount}

	fetchPost("/go", msg).then(function(res){
		console.log(res);
	})
}



function fetchPost(address, message){
  return fetch(address,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: JSON.stringify(message)
  }).then(response => response.json()).then(function(response){
    return response;
  }).catch(function(error){
  	console.log(error);
  })
}