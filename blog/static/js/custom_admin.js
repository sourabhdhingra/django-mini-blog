document.addEventListener("change", setSlugToUserName );

function setSlugToUserName() {
    var select = document.getElementById("id_user");
    if(select.selectedIndex != 0) {
        var selectedUser = select.options[select.selectedIndex].text;
        document.getElementById("id_slug").value = selectedUser;
    }
}
