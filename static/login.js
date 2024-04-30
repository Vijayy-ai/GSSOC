// // Initialize the Google Auth object
// var auth2;

// // Load the Google API client library and the Google Auth library
// function loadGoogleApi() {
//     gapi.load('client:auth2', initGoogleAuth);
// }

// // Initialize the Google Auth object
// function initGoogleAuth() {
//     gapi.client.init({
//         clientId: 'YOUR_GOOGLE_CLIENT_ID', // Replace with your Google Client ID
//         scope: 'profile email'
//     }).then(function () {
//         auth2 = gapi.auth2.getAuthInstance();

//         // Listen for sign-in state changes
//         auth2.isSignedIn.listen(updateSigninStatus);

//         // Handle the initial sign-in state
//         updateSigninStatus(auth2.isSignedIn.get());
//     });
// }

// // Handle the sign-in state change
// function updateSigninStatus(isSignedIn) {
//     if (isSignedIn) {
//         // Get the user's profile information and display it
//         var profile = auth2.currentUser.get().getBasicProfile();
//         var userName = profile.getName();
//         var userEmail = profile.getEmail();
//         var userProfileImage = profile.getImageUrl();

//         // Display the user's profile information
//         document.getElementById('user-name').textContent = userName;
//         document.getElementById('user-email').textContent = userEmail;
//         document.getElementById('user-profile-image').src = userProfileImage;

//         // Hide the sign-in button and show the sign-out button
//         document.getElementById('sign-in-button').style.display = 'none';
//         document.getElementById('sign-out-button').style.display = 'block';
//     } else {
//         // Hide the user's profile information
//         document.getElementById('user-name').textContent = '';
//         document.getElementById('user-email').textContent = '';
//         document.getElementById('user-profile-image').src = '';

//         // Show the sign-in button and hide the sign-out button
//         document.getElementById('sign-in-button').style.display = 'block';
//         document.getElementById('sign-out-button').style.display = 'none';
//     }
// }

// // Handle the sign-in button click
// function signIn() {
//     auth2.signIn();
// }

// // Handle the sign-out button click
// function signOut() {
//     auth2.signOut();
// }