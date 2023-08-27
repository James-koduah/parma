let current_dashboard = document.getElementById('register_staff') // This cointains the current dashboard element
/**
 * display_dashboard - Controls which dashboard would be displayed
 * @e: The menu item to be clicked
 */
function display_dashboard(e){
	current_dashboard.style.display = 'none'
	let dashboard = e.dataset.dashboard
	dashboard = document.getElementById(dashboard)
	dashboard.style.display = 'flex';
	current_dashboard = dashboard
	
	let menu_item = document.getElementsByClassName('menu_item')
	for (i=0; i < menu_item.length; i++){
		menu_item[i].classList.remove('active')
	}
	e.classList.add('active')
}



function send_invite(hospital_id){
	let role = document.querySelector('input[name="role"]:checked');
	let job_description = document.getElementById('invite_job_description');
	let invite_username = document.getElementById('invite_username');
	let url = '/admin/invite_staff'
	fetch(url, {
		headers : {'Content-Type' : 'application/json'},
		method : 'POST',
		body : JSON.stringify({
			"role": role.value,
			"job_description": job_description.value,
			"invite_username": invite_username.value,
			"hospital_id": hospital_id
		})
	})
	.then((response)=>{return response.json()})
	.then((json)=>{
		console.log(json['response'])
		job_description.value=''
		invite_username.value=''
	})
}
