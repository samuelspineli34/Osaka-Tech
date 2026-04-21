// frontend/src/utils/loader.ts
export const hideLoader = () => {
    const loader = document.getElementById('global-loader');
    if (loader) {
        loader.style.display = 'none';
    }
};

export const showLoader = () => {
    const loader = document.getElementById('global-loader');
    if (loader) {
        loader.style.display = 'flex';
    }
};