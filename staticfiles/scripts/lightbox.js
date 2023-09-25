function openLightbox(imageSrc) {
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightbox-image');

    lightboxImage.src = imageSrc;
    lightbox.style.display = 'flex';
    
    console.log('Opened lightbox for:', imageSrc);
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    lightbox.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', () => {
    const lightboxTriggers = document.querySelectorAll('.lightbox-trigger');

    lightboxTriggers.forEach((trigger) => {
        trigger.addEventListener('click', () => {
            const imageSrc = trigger.getAttribute('src');
            openLightbox(imageSrc);
            
            console.log('Clicked thumbnail with src:', imageSrc);
        });
    });
});