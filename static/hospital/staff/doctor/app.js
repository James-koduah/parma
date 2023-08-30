let current_dashboard = document.getElementById('appointments')
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
