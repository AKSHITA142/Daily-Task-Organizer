function showEditBox(taskId) {
    let form = document.getElementById("edit-form-" + taskId);
    if (form.style.display === "none") {
        form.style.display = "inline-block";  // show edit form
    } else {
        form.style.display = "none";  // hide if clicked again
    }
}