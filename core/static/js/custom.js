/*********************************/
/*          jQuery code          */
/*********************************/
$(document).ready(function(){
// jQuery code inside this method

//Sortable (tables)
const selectedItems = document.getElementById('drag-items')

new Sortable(selectedItems, {
    animation: 350,
//    chosenClass: "sortable-chosen",
//    dragClass: "sortable-drag",
    store: {
    	// We keep the order of the list
    	set: (sortable) =>{
    		const order = sortable.toArray()
    		localStorage.setItem(sortable.options.group.name, order.join('|'))
    	},

    	// We get the order of the list
    	get: (sortable) =>{
    		const order = localStorage.getItem(sortable.options.group.name)
    		return order ? order.split('|') : []
    	}
    }
});






});

/*********************************/
/*        JavaScript code        */
/*********************************/

//collapses/expands single task
function showHide_id(id) {
    var x = document.getElementById("task-row2-id-"+id);
    if (x.style.display === "none") {
        x.style.display = "flex";
    } else {
        x.style.display = "none";
    }

    var y = document.getElementById("task-row3-id-"+id);
    if (y.style.display === "none") {
        y.style.display = "flex";
    } else {
        y.style.display = "none";
    }
}

//collapses all tasks
function collapse_all() {
    var x = document.querySelectorAll(".task-container-row2, .task-container-row3");
    var i;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
        }
}

//expands all tasks
function expand_all() {
    var x = document.querySelectorAll(".task-container-row2, .task-container-row3");
    var i;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "flex";
        }
}


