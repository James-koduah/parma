let current_dashboard = document.getElementById('register_staff') // This cointains the current dashboard element
/**
 * display_dashboard - Controls which dashboard would be displayed
 * @e: The menu item to be clicked
 */
function display_dashboard(e){
	current_dashboard.style.display = 'none'
	let dashboard = e.dataset.dashboard
	dashboard = document.getElementById(dashboard)
	dashboard.style.display = 'block';
	current_dashboard = dashboard
	
	let menu_item = document.getElementsByClassName('menu_item')
	for (i=0; i < menu_item.length; i++){
		menu_item[i].classList.remove('active')
	}
	e.classList.add('active')
}
