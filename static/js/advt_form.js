
 function hide(){
      document.getElementById('apartment_form').style.display="block";
      document.getElementById('hostel_form').style.display="none";
      document.getElementById('house_form').style.display="none";
    }
    function f(){
    var s = document.getElementById('select_category_house').value;

  if(s=="1"){
    document.getElementById('apartment_form').style.display="block";
    document.getElementById('hostel_form').style.display="none";
    document.getElementById('house_form').style.display="none";
	document.getElementById("name_apartment").value="Apartment";



  }
  if(s=="2"){
    document.getElementById('apartment_form').style.display="none";
    document.getElementById('hostel_form').style.display="block";
    document.getElementById('house_form').style.display="none";
	document.getElementById("name_hostel").value="Hostels";

  }
  if(s=="3"){
    document.getElementById('apartment_form').style.display="none";
    document.getElementById('hostel_form').style.display="none";
    document.getElementById('house_form').style.display="block";
	document.getElementById("name_house").value="House";

  }

  }
