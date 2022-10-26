


function print(){
	var name = document.getElementById('name').value;
	var reference = document.getElementById('reference').value;
	var chequeNo = document.getElementById('chequeNumber').value;
	var amount = document.getElementById('amount').value;
	let msg = {"name": name,"reference": reference, "chequeNo": chequeNo, "amount": amount}

	fetchPost("/go", msg).then(function(res){
		console.log(res);
    let url = '/cheque/' + name + '/' + reference + '/' + chequeNo + '/' + '£' + amount
    window.open(url, 'popup')
    window.location.reload(true)
	})
}

function print_prew(e){
  let par = e.parentElement.parentElement;
  let url = 'cheque/' + par.children[0].innerText + '/' + par.children[1].innerText + '/' + par.children[2].innerText + '/' + par.children[3].innerText
  window.open(url)
}

var chequeDate
var oldNo

function edit(e){
  let par = e.parentElement.parentElement;
  let clientRect = par.getBoundingClientRect();
  let form = document.getElementById('editForm');
  form.children[0].value = par.children[0].innerText;
  form.children[1].value = par.children[1].innerText;
  form.children[2].value = par.children[2].innerText;
  form.children[3].value = par.children[3].innerText.slice(2);
  chequeDate = par.children[4].innerText;
  oldNo = par.children[2].innerText;
  let left = (clientRect.left + document.body.scrollLeft) * 0.9;
  form.style.left = left.toString() + 'px';
  form.style.top = (clientRect.top + document.body.scrollTop).toString() + 'px';
  console.log('this', clientRect.left);
  document.getElementById('cover').style.visibility = "visible";
  form.style.visibility = 'visible';
}

function allert(where, msg, color){
  let holder = document.getElementById(where);
  holder.style.display = 'inline-block'
  holder.style.color = color;
  holder.innerText = msg;
}

function editSub(){
  let form = document.getElementById('editForm');
  var name = form.children[0].value;
  var reference = form.children[1].value;
  var chequeNo = form.children[2].value;
  var amount = form.children[3].value;
  console.log('date', chequeDate);
  let msg = {"name": name,"reference": reference, "chequeNo": chequeNo, "amount": amount, "checqueDate" : chequeDate, 'oldNo': oldNo}
  console.log('msg',msg);
  fetchPost("/edit", msg).then(function(res){
    console.log(res);
    if (res['Success'] == true){
      allert('message_edit', res['msg'], 'green');
      setTimeout(function(){window.location.reload(true)},300);
    }
  })
}

function canc(){
  document.getElementById('editForm').style.visibility = 'hidden';
  document.getElementById('cover').style.visibility = "hidden";
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

var escKey = document.addEventListener("keyup", function(event) {
  if (event.keyCode === 27) {
    canc();
  }
});