import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { debounceTime, tap, filter } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';
import { FileUploadService } from 'src/app/services/file-upload.service';
import { faHandPointRight, faTimesCircle } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.scss']
})
export class SearchPageComponent implements OnInit {
  activeTab = 1;
  uploading = false;
  queryingWikipedia = false;

  searchForm: FormGroup;
  queryResults: any;
  selectedQueryResults = [];
  selectedFile: File;
  articleData = [];

  faHandPointRight = faHandPointRight;
  faTimesCircle = faTimesCircle;

  constructor(
    private _fb: FormBuilder, 
    private _httpClient: HttpClient,
    private _fileUploadService: FileUploadService) { }

  ngOnInit() {
    this.searchForm = this._fb.group({
      searchBox: '',
      reportQueryText: ''
    });

    const queryResult$ = this.searchForm.controls['searchBox'].valueChanges
      .pipe(
        filter(queryText => queryText.length >= 3),
        debounceTime(500),
        tap(() => {
          if (!!this.queryResults)
            this.queryResults.length = 0;

          this.queryingWikipedia = true;
        })
      );

    queryResult$.subscribe(finalQueryText => {
      const apiResult$ = this._httpClient.get(`http://127.0.0.1:5002/query/${finalQueryText}`);
      apiResult$.subscribe(data => {
        console.log(data);
        this.queryResults = data;
        this.queryingWikipedia = false;
      });
    });
  }

  articleClicked(articleName: string): any {
    console.log('article clicked!', articleName);
    const articleWithoutSpaces = articleName.replace('%20', ' ');
    const apiResult$ = this._httpClient.get(`http://127.0.0.1:5002/getArticle/${articleName}`);

    apiResult$.subscribe((data: any) => {
      console.log('getArticle response:', data);
      window.open(data.url, '_blank');
    });
  }

  articleSelected(articleName: string): any {
    console.log('article selected', articleName, this.queryResults);
    this.selectedQueryResults.push(articleName);
    this.queryResults = this.queryResults.filter(r => r !== articleName);
  }

  removeSelectedQueryResult(selectedQueryResult: string): any {
    this.selectedQueryResults = this.selectedQueryResults.filter(r => r !== selectedQueryResult);
  }

  handleFileInput(files: FileList) {
    console.log('SearchPageComponent.handleFileInput called, filelist data:', files);
    this.selectedFile = files[0];
  }

  startDataQuerySection() {
    const search = this;
    const articles = this.selectedQueryResults;
    let articleRetrievedIndex = 0;
    this.uploading = true;
    console.log('Articles Selected', articles);
    articles.forEach((value) => {
      console.log('Retrieving Content for:', value);
      const apiResult$ = search._httpClient.get(`http://127.0.0.1:5002/getArticleData/${value}`);

      apiResult$.subscribe((data: any) => {
        console.log('getArticleData response:', data);
        articleData.push(data);
        articleRetrievedIndex++;

        if (articleRetrievedIndex == this.selectedQueryResults.length) {
          this.uploading = false;
          this.goToTab(2);
        }
      });
    });

    const articleData = this.articleData;
    console.log('Article(s) Data', articleData);

    // if (!!this.selectedFile) {
    //   this.uploading = true;

      const postFile$ = this._fileUploadService.postFile(this.selectedFile);

    //   postFile$.subscribe((data) => {
    //     console.log('SearchPageComponent.handleFileInput postFile service call subscription returned data', data);
    //     this.goToTab(2);
    //     this.uploading = false;
    //   });
    // } else {
    //   this.goToTab(2);
    // }
  }

  performQuery() {
    const endpoint = 'http://127.0.0.1:5002/generatereport';
    const queryData = new FormData();

    if (!!this.selectedFile) {
      queryData.append('pdfFile', this.selectedFile, this.selectedFile.name);
    }

    if (!!this.articleData) {
      const encodedArticleData = JSON.stringify(this.articleData);

      console.log('encodedArticleData', encodedArticleData);

      queryData.append('articleData', encodedArticleData);
    }

    if (!!this.searchForm.controls.reportQueryText.value) {
      queryData.append('queryString', this.searchForm.controls.reportQueryText.value);
    }

    const apiResult$ = this._httpClient.post(endpoint, queryData, { headers: {} });

    apiResult$.subscribe(response => {
      console.log('performQuery POST API response', response);
    });

  }

  goToTab(tabNumber: number) {
    this.activeTab = tabNumber;
  }

  startOver() {
    this.activeTab = 1;
    this.selectedFile = null;
    this.queryResults.length = 0;
    this.articleData.length = 0;
    this.selectedQueryResults.length = 0;
    this.searchForm.controls['searchBox'].setValue('');
  }
}
