let current_dashboard = document.getElementById('current_patient')
function display_dashboard(dashboard_id, menu_item=false){
	let dashboard_item = document.getElementById(dashboard_id)
	dashboard_item.style.display='flex'
	current_dashboard.style.display='none'
	current_dashboard = dashboard_item

	if (menu_item){
		let menu_items = document.getElementsByClassName('sections_menu_item')
		for (let i=0; i < menu_items.length; i++){
			menu_items[i].classList.remove('active')
		}
		menu_item.classList.add('active')
	}
}


let light_dark = 'light'
function dark_light_mode(){
	let body = document.getElementsByTagName('body')[0] 
	let dashboard = document.getElementById('dashboard')
	if (light_dark == 'light'){
		body.style.background="#444"
		body.style.color="#eee"
		dashboard.style.background="#333"
		dashboard.style.color="#eee"
		light_dark = 'dark'
	}
	else if(light_dark == 'dark'){
		body.style.background="#eee"
		body.style.color="#444"
		dashboard.style.background="#ccc"
		dashboard.style.color="#222"
		light_dark = "light"
	}
}
dark_light_mode()


function accept_appointment(id){
	fetch('/hospital/accept_appointment/', {
		headers : {'Content-Type' : 'application/json'},
		method : 'POST',
		body : JSON.stringify({'appointment_id': id})
	})
	.then((res)=>{return res.json()})
	.then((json)=>{
		console.log(json['response'])
		if (json['response'] == 'success'){
			document.getElementById('appointment'+id).remove();
			window.location.reload(true)
		}
		count_appointments()
	})
}

function close_appointment(id){
	fetch('/hospital/close_appointment/', {
		headers : {'Content-Type' : 'application/json'},
		method : 'POST',
		body : JSON.stringify({'appointment_id': id})
	})
	.then((res)=>{return res.json()})
	.then((json)=>{
		console.log(json['response'])
		if (json['response'] == 'success'){
			window.location.reload(true)
		}
	})
}

function count_appointments(){
	let items = document.getElementsByClassName('appointments_item')
	document.getElementById('appointments_num').innerText = items.length
}
count_appointments()


