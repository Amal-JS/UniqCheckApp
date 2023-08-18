console.log('started')

//form handling frontend


//funtion to empty the div for errors when user give value in a field and then again gives another value the existing p element will remain, to remove that using this
function clear_div(name){

    if (name.charAt(0) === '#'){
        element = document.querySelector(name+"-error")
        element.textContent=''
    }else{
        element = document.querySelectorAll(name)
        elements.forEach(element => {
        // Set the text content to an empty string
        element.textContent = '';
    });
    }
    
}

//empty the form errors before submitting then only if again occurs the div will be empty
document.getElementById('signup_form').addEventListener('submit', () => {
    const elements = document.querySelectorAll('.error-container')
    // Loop through the selected elements
    clear_div('.error-container')
    
})

//form handling
document.addEventListener('DOMContentLoaded', function () {
    // Function to check if value and some another validation  in the database

    async function checkExists(fieldName, fieldValue) {

        const response = await fetch(`/validation/?field_name=${fieldName}&field_value=${fieldValue}`);
        const data = await response.json();

        if (data.exists) {

            // 'data.errors' is an object with the structure like { field_name: error_list (it is a string) }


            // const errors = data.errors;
            // const fieldN = data.errors.field_name;
            // console.log(fieldN)



            for (const field_name in errors) {

                if (errors.hasOwnProperty(field_name)) {

                    const error_list = errors[field_name];
                    
                    console.log("Field Name: " + field_name + "Error List: " + error_list);
                    
                    //getting the div element to display error
                    errorContainer = document.getElementById(fieldName + '-error')

                    //If error_list is an array, you can loop through its items
                    //checking if any element in list is ''
                    arr = error_list.split(',').filter(item => item !== '');
                    

                    if (arr) {

                        for (let i = 0; i < arr.length; i++) {

                            const errorLine = document.createElement('p');
                            console.log(error_list[i])
                            errorLine.textContent = arr[i]
                            errorLine.classList.add('text-danger','m-0', 'ml-5', 'mt-1');
                            errorContainer.appendChild(errorLine);
                            //console.log("Error " + (i + 1) + ": " + error_list[i]);
                        }
                    }
                }
            }





           
        } else {
            document.getElementById(fieldName + '-error').textContent = '';
        }
    }


    // Event listeners for each input field
    //id of input tage
    document.getElementById('id_username').addEventListener('blur', function () {

        //clear the div element again focusing on input element
        
        clear_div('#username')

        //check the value 
        checkExists('username', this.value); //this.value or document.getElementById('id_username').value
    });




    document.getElementById('id_email').addEventListener('blur', function () {
        clear_div('#email')
        checkExists('email', document.getElementById('id_email').value);
    });


    
    document.getElementById('id_phone').addEventListener('blur', function () {
        clear_div('#phone')
        checkExists('phone', document.getElementById('id_phone').value);
    });
});