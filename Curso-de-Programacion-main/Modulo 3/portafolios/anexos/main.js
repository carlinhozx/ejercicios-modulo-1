/*=============== SHOW MENU ===============*/

/*===== MENU SHOW =====*/
/* Validate if constant exists */

/*===== MENU HIDDEN =====*/
/* Validate if constant exists */

/*==================== REMOVE MENU MOBILE ====================*/

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/

/*==================== CHANGE BACKGROUND HEADER ====================*/

/*==================== SHOW SCROLL UP ====================*/

/*==================== ABOUT TABS ====================*/
const tabs = document.querySelectorAll('[data-target]'),
      tabContents = document.querySelectorAll('[data-content]');  // "Document" con mayúscula cambiado a "document"

tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.target);  // "tad" cambiado a "tab"
        
        tabContents.forEach((tabContent) => {  // "tabContents" cambiado a "tabContent" para evitar confusión
            tabContent.classList.remove('tab_active');  // "classlist" cambiado a "classList"
        });
        
        target.classList.add('tab_active');  // "classlist" cambiado a "classList"
        
        tabs.forEach((tab) => {  // "tabs-forEach" cambiado a "tabs.forEach"
            tab.classList.remove('tab_active');  // "classlist" cambiado a "classList"
        });
        
        tab.classList.add('tab_active');  // "classlist" cambiado a "classList"
    });
});

/*=============== CONTACT FORM =============== */
