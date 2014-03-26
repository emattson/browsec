function setViewport(img, x, y, width, height) {
    img.style.left = "-" + x + "px";
    img.style.top  = "-" + y + "px";

    if (width !== undefined) {
        img.parentNode.style.width  = width  + "px";
        img.parentNode.style.height = height + "px";
    }
}
