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
  searchForm: FormGroup;
  queryResults: any;
  selectedQueryResults = [];
  selectedFile: File;

  faHandPointRight = faHandPointRight;
  faTimesCircle = faTimesCircle;

  constructor(
    private _fb: FormBuilder, 
    private _httpClient: HttpClient,
    private _fileUploadService: FileUploadService) { }

  ngOnInit() {
    this.searchForm = this._fb.group({
      searchBox: ''
    });

    const queryResult$ = this.searchForm.controls['searchBox'].valueChanges
      .pipe(
        filter(queryText => queryText.length >= 3),
        debounceTime(500),
        tap(queryText => console.log(queryText))
      );

    queryResult$.subscribe(finalQueryText => {
      const apiResult$ = this._httpClient.get(`http://127.0.0.1:5002/query/${finalQueryText}`);
      apiResult$.subscribe(data => {
        console.log(data);
        this.queryResults = data;
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

  handleFileInput(files: FileList) {
    console.log('SearchPageComponent.handleFileInput called, filelist data:', files);
    this.selectedFile = files[0];
  }

  uploadFile() {
    this._fileUploadService.postFile(this.selectedFile)
      .pipe(
        tap(streamData => console.log('SearchPageComponent.handleFileInput postFile service call returned data:', streamData)))
      .subscribe((data) => console.log('SearchPageComponent.handleFileInput postFile service call subscription returned data', data));
  }
}
