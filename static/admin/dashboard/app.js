/**
 * display_dashboard - Controls which dashboard would be displayed
 * @e: The menu item to be clicked
 */
let current_dashboard = document.getElementById('register_staff') // This cointains the current dashboard element
function display_dashboard(dashboard_id, menu_item=false){
	dashboard = document.getElementById(dashboard_id)
	dashboard.style.display = 'flex';
	current_dashboard.style.display = 'none'
	current_dashboard = dashboard
	
	if (menu_item){
		let menu_items = document.getElementsByClassName('menu_item')
		for (i=0; i < menu_items.length; i++){
			menu_items[i].classList.remove('active')
		}
		menu_item.classList.add('active')
	}
}



function send_invite(hospital_id){
	popup_display('Sending Invite...')
	let role = document.querySelector('input[name="role"]:checked');
	let job_description = document.getElementById('invite_job_description');
	let invite_username = document.getElementById('invite_username');
	let url = '/admin/invite_staff'
	if (job_description.value == ''){
		return popup_display('Provide a Job description')
	}
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
		popup_display(json['response'])
		job_description.value=''
		invite_username.value=''
	})
}


function confirm_staff(invite_id){
	let url='/admin/confirm_staff_invite'
	fetch(url, {
		headers : {'Content-Type' : 'application/json'},
		method : 'POST',
		body : JSON.stringify({"invite_id": invite_id})
	})
	.then((res)=>{return res.json()})
	.then((json)=>{
		popup_display(json['response'])
		window.location.reload(true)
	})
}

let popup = document.getElementById('response_status')
let popup_text = document.getElementById('response_status_text')
function popup_display(text){
	popup.style.display = 'flex'
	popup_text.innerHTML = text
}
function popup_display_close(){
	popup.style.display = 'none'
}



document.getElementById('invite_job_description').addEventListener('keydown', (e)=>{
	if (e.keyCode == 13){
		document.getElementById('invite_username').focus()
	}
})
document.getElementById('invite_username').addEventListener('keydown', (e)=>{
	if (e.keyCode == 13) send_invite();		
})
