const tooltips = {
    fb_messenger: "FB Messenger",
    home: "Home of WebWise",
    discord: "Discord",
    signIn: "Sign In",
    signUp: "Sign Up",
    github: "GitHub",
    close: "close",
    fb: "Facebook",
    email: "Email",
    
};
Object.keys(tooltips).forEach((e) => {
    const o = document.querySelectorAll(`[tippy="${e}"]`);
    // tippy.js for 𝘴𝘩𝘦𝘦𝘴𝘩𝘢𝘣𝘭𝘦 tooltips
    o && tippy(o, { content: tooltips[e] });
});
