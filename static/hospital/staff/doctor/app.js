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
	if (light_dark == 'light'){
		body.style.background="#444"
		body.style.color="#eee"
		light_dark = 'dark'
	}
	else if(light_dark == 'dark'){
		body.style.background="#eee"
		body.style.color="#444"
		light_dark = "light"
	}
}
