const allCheckBoxForms = document.querySelectorAll('li form');
const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]');
const projectId = document.getElementById('projectId').getAttribute('data-project-id');
const markAsCompletedBtn = document.getElementById('markAsCompleted')
const cancelPopupBtn = document.getElementById('cancel_popup_btn');
const cancelGroupDeletionPopupBtn = document.getElementById('cancel_group_deletion_btn');
const continuePopupBtn = document.getElementById('continue_popup_btn');
const popupOverlay = document.getElementById('complete_project_overlay');
const projectComment = document.getElementById('project_comment');
const upgradableRadioBtns = document.querySelectorAll('input[name="upgradable"]');

const createNewMemberBtn = document.getElementById("create_single_member");
const createMemberPopupOverlay = document.getElementById("create_member_overlay");

const deleteGroupBtn = document.getElementById("delete_group_btn");
const deletGroupOverLay = document.getElementById("delete_group_overlay")




let allCheckValues = {};
let completionLevel = 0;

allCheckBoxForms.forEach(checkBoxForm =>{
    const checkInput = checkBoxForm.querySelector('input[type="checkbox"]');
    const projectStep = parseInt(checkInput.getAttribute('data-step-no'));
    allCheckValues[projectStep] = checkInput.checked;
    if(checkInput.checked){
        completionLevel = projectStep
    };
    checkInput.addEventListener('click', async ()=>{
            allCheckValues[projectStep] = checkInput.checked;
            console.log(checkInput.checked);
            const request = new Request(`/complete-project-step/${projectId}`, {
                method:'POST',
                headers:{
                    'X-CSRFToken':csrfToken.value
                },
                body:JSON.stringify({'lastChecked':projectStep})
            });

            const response = await fetch(request);
            if(response.redirected){
                window.location.href = response.url
            }
            else{
                alert('Something went wrong !')
        }
    })
})


async function markAsCompleted(){
            
    const checkedRadio = [...upgradableRadioBtns].filter(radioBtn =>{
        return radioBtn.checked === true
    });
    const checkedValue = checkedRadio[0].value;
    const prjCommentContent = projectComment.value;
            const request = new Request(`/mark-as-completed/${projectId}`, {
                method:'POST',
                headers:{
                    'X-CSRFToken':csrfToken.value
                },
                body:JSON.stringify({'completionLevel':completionLevel, 'projectComment':prjCommentContent, 'upgradable':checkedValue})
            });

            const response = await fetch(request);
            if(response.redirected){
                window.location.href = response.url
            }
            else{
                alert('Something went wrong !')
        }
}

function showPopup(){
    popupOverlay.style.display = 'inline-block';
}

function dismissOverlays(){
    const allOverlays = document.querySelectorAll(".popup-overlay");
    allOverlays.forEach(overlay =>{
        overlay.style.display = 'none';
    })   
}

const allOverlays = document.querySelectorAll(".popup-overlay");
    allOverlays.forEach(overlay =>{
        overlay.addEventListener('click', (e)=>{
            if(e.target.classList.contains('popup-container') || e.target.classList.contains('popup-overlay')){
                dismissOverlays();
            }
        })
    })   


try {
    cancelPopupBtn.addEventListener('click', ()=>{
        dismissOverlays()
    });
} catch (error) {
    console.warn(error);
}

cancelGroupDeletionPopupBtn.addEventListener('click', ()=>{
    dismissOverlays();
})


cancelPopupBtn.addEventListener('click', ()=>{
    dismissOverlays()
});

try {
    markAsCompletedBtn.addEventListener('click', showPopup);
} catch (error) {
    console.warn(error);
}

try {
    continuePopupBtn.addEventListener('click', markAsCompleted);
} catch (error) {
    console.warn(error);
}

try {
    createNewMemberBtn.addEventListener('click', ()=>{
        createMemberPopupOverlay.style.display = 'inline-block';
    })
} catch (error) {
    console.warn(error)
}

try {
    deleteGroupBtn.addEventListener('click', ()=>{
        deletGroupOverLay.style.display = 'inline-block';
    })
} catch (error) {
    console.warn(error)
}
