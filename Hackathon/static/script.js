document.addEventListener('DOMContentLoaded', function () {
    const instagramInput = document.getElementById('instagram-address');
    const analyzeButton = document.getElementById('analyze-button');
    const imageOutput = document.querySelector('.image-output img');
    const emotionCounter = document.querySelector('.emotion-counter ul');
    const postPreviews = document.querySelector('.post-previews');

    analyzeButton.addEventListener('click', function () {
        const instagramAddress = instagramInput.value.trim();
        // 인스타그램 주소를 분석하여 결과를 가져오는 로직을 구현합니다.
        // 이 예제에서는 간단하게 랜덤 결과를 생성합니다.
        const results = generateRandomEmotionResults();
        updateResults(results);
    });

    function generateRandomEmotionResults() {
        // 임의의 감정 결과를 생성하여 반환합니다.
        return {
            joy: Math.floor(Math.random() * 10),
            anger: Math.floor(Math.random() * 10),
            pleasure: Math.floor(Math.random() * 10),
        };
    }

    function updateResults(results) {
        // 결과를 화면에 표시합니다.
        imageOutput.src = 'https://via.placeholder.com/400'; // 임의의 이미지 URL
        emotionCounter.innerHTML = '';
        for (const emotion in results) {
            const count = results[emotion];
            const li = document.createElement('li');
            li.textContent = `${emotion}: ${count}`;
            emotionCounter.appendChild(li);
        }

        // 게시물 미리보기를 업데이트합니다.
        postPreviews.innerHTML = '';
        for (let i = 0; i < 3; i++) {
            const postThumbnail = document.createElement('div');
            postThumbnail.className = 'post-thumbnail';
            const img = document.createElement('img');
            img.src = 'https://via.placeholder.com/400'; // 임의의 이미지 URL
            postThumbnail.appendChild(img);
            postPreviews.appendChild(postThumbnail);
        }
    }
});

// Image upload functionality
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            document.querySelector('.image-upload-wrap').style.display = 'none';
            document.querySelector('.file-upload-image').src = e.target.result;
            document.querySelector('.file-upload-content').style.display = 'block';
            document.querySelector('.image-title').textContent = input.files[0].name;
        };

        reader.readAsDataURL(input.files[0]);

    } else {
        removeUpload();
    }
}

function removeUpload() {
    document.querySelector('.file-upload-input').parentNode.replaceChild(document.querySelector('.file-upload-input').cloneNode(true), document.querySelector('.file-upload-input'));
    document.querySelector('.file-upload-content').style.display = 'none';
    document.querySelector('.image-upload-wrap').style.display = 'block';
}

document.querySelector('.image-upload-wrap').addEventListener('dragover', function () {
    document.querySelector('.image-upload-wrap').classList.add('image-dropping');
});

document.querySelector('.image-upload-wrap').addEventListener('dragleave', function () {
    document.querySelector('.image-upload-wrap').classList.remove('image-dropping');
});