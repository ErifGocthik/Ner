(function download() {
    $(document).ready(function () {
        let imageId = '';
        $(document).on('click', '.download', function () {
            imageId = $('.window_image_detail_id').attr('class').split(' ')[1].split('_')[2];
            document.location.pathname = `/image/${imageId}/download/`;
        });
    });
})();