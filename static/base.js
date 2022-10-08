


function print(){
	var name = document.getElementById('name').value;
	var reference = document.getElementById('reference').value;
	var chequeNo = document.getElementById('chequeNumber').value;
	var amount = document.getElementById('amount').value;
	let msg = {"name": name,"reference": reference, "chequeNo": chequeNo, "amount": amount}

	fetchPost("/go", msg).then(function(res){
		console.log(res);
    let url = '/cheque/' + name + '/' + reference + '/' + chequeNo + '/' + amount
    window.open(url, 'popup')
    window.location.reload(true)
	})
}

function print_prew(e){
  let par = e.parentElement.parentElement;
  let url = 'cheque/' + par.children[0].innerText + '/' + par.children[1].innerText + '/' + par.children[2].innerText + '/' + par.children[3].innerText
  window.open(url)
}


function fetchPost(address, message){
  return fetch(address,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(message)
  }).then(response => response.json()).then(function(response){
    return response;
  }).catch(function(error){
  	console.log(error);
  })
}

var startKey = document.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    print();
  }
});