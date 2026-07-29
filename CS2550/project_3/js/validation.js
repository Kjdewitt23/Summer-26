/* validation.js - Form validation library */

// TODO: Find a suitable phone number regex and place it here
let phoneRegex = /^(\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$/;
let emailRegex = /[\w]*@[\w]*.{1}(com|gov|edu|io|net){1}/;
let zipCodeRegex = /(^\d{5}$)|(^\d{5}-\d{4}$)/;

const stateAbbreviations = [
    'AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA',
    'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA',
    'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
    'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
    'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY'
];

let form = null;
let successMsg = null;

function initValidation(formId, successId) {
    form = document.getElementById(formId);
    successMsg = document.getElementById(successId);

    // Bind the 'change' event to all inputs
    let inputs = document.querySelectorAll("input");
    for (let input of inputs) {
        input.addEventListener("change", inputChanged);
    }

    form.addEventListener("submit", submitForm);
}

function submitForm(ev) {
    // Prevent the browser from naturally submitting the form and refreshing the page
    ev.preventDefault();
    ev.stopPropagation();

    validateForm();

    if (!form.checkValidity()) {
        let inputs = document.querySelectorAll("input");

        for (let input of inputs) {
            input.classList.add("was-validated");
        }
    } else {
        form.style.display = "none";
        successMsg.style.display = "block";
    }
}

function validateForm() {
    checkRequired("first-name", "First Name is Required");
    checkRequired("last-name", "Last Name is Required");
    checkRequired("address", "Address is Required");
    checkRequired("city", "City is Required");

    if (checkRequired("state", "State is Required")) {
        validateState("state", "Not a valid State, enter two digit code e.g., UT");
    }

    if (checkRequired("email", "Email Address is required")) {
        checkFormat("email", "Email format is bad", emailRegex);
    }
    if (checkRequired("zip", "Zip Code is Required")) {
        checkFormat("zip", "Malformed zip-code, please use 5 or 9 digit format.", zipCodeRegex);
    }
    if (checkRequired("phone", "Phone is required")) {
        checkFormat("phone", "Phone format is bad", phoneRegex);
    }

    checkRequired("newspaper", "You must select at least one referral method!");
}

function validateState(id, msg) {
    let el = document.getElementById(id);
    let valid = false;

    let value = el.value.toUpperCase();
    valid = stateAbbreviations.includes(value);

    setElementValidity(id, valid, msg);
}

function checkFormat(id, msg, regex) {
    let el = document.getElementById(id);
    let valid = false;

    valid = regex.test(el.value);

    setElementValidity(id, valid, msg);
    return valid;
}

function checkRequired(id, message) {
    let el = document.getElementById(id);
    let valid = false;
    let type = el.type;

    switch (type) {
        case 'text':
        case 'email':
        case 'password':

            valid = el.value.trim() !== "";
            break;

        case 'checkbox':
        case 'radio':

            let checked = document.querySelectorAll(
                `input[name="${el.name}"]:checked`
            );

            valid = checked.length > 0;

            break;
    }

    setElementValidity(id, valid, message);
    return valid;
}

function setElementValidity(id, valid, message) {
    let el = document.getElementById(id);
    let errorDiv = el.parentNode.querySelector('.errorMsg');

    if (valid) {
        // Sets to no error message and field is valid
        el.setCustomValidity('');
        errorDiv.textContent = "";

    } else {
        // Sets error message and field gets 'invalid' stat
        el.setCustomValidity(message);
        errorDiv.textContent = message;

    }
}