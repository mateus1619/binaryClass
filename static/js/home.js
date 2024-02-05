

$('.demo').squeezebox({
  timing:300
});


player = new Plyr('#player');


// quando clicar em algum item no accordion
accordion = document.getElementById('squeezecnt')
accordion.onclick = (e) => {

  (async () =>{
    let id = e.target.id
    try {
      const response = await fetch('/videos/' + id.toString());

      if (!response.ok) {
        throw new Error('Erro ao obter os dados');
      }

      const data = await response.json();

      let videoSources = new Array();
      let videoQuality = new Array();

      for(const element of data.videos){
        reso = element.resolution
        url = element.url

        videoSources.push({src: url,type: 'video/mp4',size: reso});
        videoQuality.push(parseInt(reso))
      }

      player.quality = [720, 360]
      player.source = {
        type: 'video',
        title: 'Example title',
        sources: videoSources,
        poster: 'https://cdn.plyr.io/static/demo/View_From_A_Blue_Moon_Trailer-HD.jpg',
        previewThumbnails: {
          src: '/path/to/thumbnails.vtt',
        }
      };
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  })();

});
