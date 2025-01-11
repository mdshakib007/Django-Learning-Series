const loadProfile = () => {
    const uid = localStorage.getItem('user_id');
    fetch(`https://smartcarebd-backend.onrender.com/user/list/?user_id=${uid}`)
        .then(res => res.json())
        .then(data => {
            const profileContainer = document.getElementById('profile-container');
            const user = data[0]; // Assuming there's only one user in the response

            if (user) {
                // Create profile details dynamically
                profileContainer.innerHTML = `
                    <div class="flex items-center space-x-4">
                        <img src="./images/profile.png" alt="Profile Picture" class="w-20 h-20 rounded-full border border-violet-300">
                        <div>
                            <h2 class="text-xl font-semibold">${user.first_name} ${user.last_name}</h2>
                            <p class="text-sm text-gray-500">@${user.username}</p>
                        </div>
                    </div>
                    <div>
                        <h3 class="text-lg font-medium text-gray-700">Email:</h3>
                        <p class="text-gray-600">${user.email}</p>
                    </div>
                `;
            } else {
                profileContainer.innerHTML = `
                    <p class="text-center text-red-500">User data not found.</p>
                `;
            }
        })
        .catch(error => {
            console.error('Error fetching user profile:', error);
            document.getElementById('profile-container').innerHTML = `
                <p class="text-center text-red-500">Failed to load profile. Please try again later.</p>
            `;
        });
};

loadProfile();
