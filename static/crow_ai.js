document.addEventListener("DOMContentLoaded", function () {
    const crowSound = new Audio("/static/crow.mp3");

    // Find the last crow message and apply effects
    const chatBubbles = document.querySelectorAll(".message.crow");
    if (chatBubbles.length > 0) {
        const lastCrowMessage = chatBubbles[chatBubbles.length - 1];

        // Delay crow message appearance with "typing..." effect
        const originalMessage = lastCrowMessage.textContent;
        lastCrowMessage.textContent = "Crow is typing...";
        lastCrowMessage.classList.add("typing");

        setTimeout(() => {
            lastCrowMessage.textContent = originalMessage;
            lastCrowMessage.classList.remove("typing");
            lastCrowMessage.classList.add("pop-in");

            // Play crow sound
            crowSound.play();
        }, 1200);  // Adjust typing duration as needed
    }
});
