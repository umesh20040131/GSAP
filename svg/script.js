// Guitar string vibration animation
const svg = document.querySelector("svg");
const path = document.querySelector("path");

// Initial path points (from the SVG)
const start = { x: 10, y: 80 };
const end = { x: 180, y: 80 };
const control = { x: 95, y: 10 }; // initial control point

function updateString(ctrlY) {
  // Update the path's 'd' attribute to animate the control point's Y value
  path.setAttribute(
    "d",
    `M${start.x} ${start.y} Q ${control.x} ${ctrlY} ${end.x} ${end.y}`
  );
}

// Animate the string on click
svg.addEventListener("click", () => {
  gsap.to(control, {
    y: 60, // how far the string vibrates
    duration: 0.1,
    yoyo: true,
    repeat: 20, // number of vibrations
    ease: "elastic.out(1, 0.3)",
    onUpdate: () => updateString(control.y),
    onComplete: () => updateString(10) // reset to original
  });
});
