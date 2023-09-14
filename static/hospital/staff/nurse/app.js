let current_dashboard = document.getElementById('appointments')
function display_dashboard(dashboard_id, menu_item=false){
	let dashboard_item = document.getElementById(dashboard_id)
	dashboard_item.style.display='flex'
	current_dashboard.style.display='none'
	current_dashboard = dashboard_item

	if (menu_item){
		let menu_items = document.getElementsByClassName('side_menu_item')
		for (let i=0; i < menu_items.length; i++){
			menu_items[i].classList.remove('active')
		}
		menu_item.classList.add('active')
	}
}


let appointments_doctor_display_toogle = false;
function appointments_doctor_display(){
	let display = document.getElementById('appointments_doctor_display')
	if (appointments_doctor_display_toogle == false){
		display.style.display = 'block'
		appointments_doctor_display_toogle = true
	}
	else{
		display.style.display = 'none';
		appointments_doctor_display_toogle = false;
	}
}

function set_appointment(hospital_id){
	let patient_id = document.getElementById('appointments_patients_id').value
	let info = document.getElementById('illness_description').value
	fetch('/hospital/set_appointment', {
		headers : {'Content-Type': 'application/json'},
		method : 'POST',
		body : JSON.stringify({
			"patientId" : patient_id,
			"hospitalId" : hospital_id, 
			"info" : info
		})
	})
	.then((res)=>{return res.json()})
	.then((json)=>{
		display_message(json['response'])
		document.getElementById('appointments_patients_id').value=''
                document.getElementById('illness_description').value=''

	})
}


function add_patient(hospital_id){
	let patient_name = document.getElementById('patients_add_name').value
	let national_id = document.getElementById('patients_add_national_id').value
	let birth_date = document.getElementById('patients_add_birth_date').value
	let contact = document.getElementById('patients_add_contact').value
	if (
		patient_name == ''||
		national_id == '' ||
		birth_date == ''  ||
		contact == ''
	){
		console.log('blank feild')
		return
	}
	fetch('/hospital/add_patient', {
		headers : {'Content-Type': 'application/json'},
		method : 'POST',
		body : JSON.stringify({
			"patient_name" : patient_name,
			"national_id" : national_id,
			"birth_date" : birth_date,
			"contact" : contact,
			"hospital_id": hospital_id
		})
	})
	.then((res)=>{return res.json()})
	.then((json)=>{
		let displa = document.getElementById('patients_add_success')
		let display = document.getElementById('patients_add_success_message')
		displa.style.display='flex'
		if (json['status'] == 'success'){
			display.innerHTML = `Success, Patient's ID is <br> ${json['response']}` 
		}
		else if(json['status'] == 'error'){
			display.innerHTML = `Error, ${json['response']}`
		}
	})
}
function search_patient(){
	let search_string = document.getElementById('patients_searchbox').value
	let display = document.getElementById('patients_search_results')
	display.innerHTML = ''
	function patient_html(name, national_id, patient_id, contact){
		let html=`<div class='patient_search_item'>\
			    <div class='patient_search_item_img'></div>\
			    <div class='patient_search_item_info'>\
			    	<p>${name}</p>\
				<p>National ID: ${national_id}</p>\
				<p>Patient ID: ${patient_id}</p>\
				<p>Contact: ${contact}</p>\
			    </div>\
		    	  </div>\
		    	 `
		return html
	}
	fetch('/hospital/search_patient', {
		headers : {'Content-Type' : 'application/json'},
		method : 'POST',
		body: JSON.stringify({"search_string": search_string})
	})
	.then((res)=>{return res.json()})
	.then((json)=>{
		let results = json['response']
		for (let i=0; i < results.length; i++){
			let patient = results[i]
			let name = patient['name']
			let national_id = patient['national_id']
			let patient_id = patient['id']
			let contact = patient['contact']
			let inject = patient_html(name, national_id, patient_id, contact)
			display.innerHTML += inject
		}
	})
}

function close_display(id){
	let item = document.getElementById(id).style.display='none'
}

function close_hidden(e){
	e.style.display = 'none'
}
function display_message(message){
	let hidden = document.getElementById('hidden')
	let popup_message = document.getElementById('popup_message')
	popup_message.innerHTML = message
	hidden.style.display='flex';
	hidden.style.zIndex=100;
}
	

document.getElementById('patients_searchbox').addEventListener('keydown', (e)=>{
	if (e.keyCode == 13){
		search_patient()
	}
})
