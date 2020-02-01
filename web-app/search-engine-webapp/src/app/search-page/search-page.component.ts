import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { debounceTime, tap, filter } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.scss']
})
export class SearchPageComponent implements OnInit {
  searchForm: FormGroup;
  queryResults: any;

  constructor(private _fb: FormBuilder, private _httpClient: HttpClient) { }

  ngOnInit() {
    this.searchForm = this._fb.group({
      searchBox: ''
    })

    let queryResult$ = this.searchForm.controls['searchBox'].valueChanges
      .pipe(
        filter(queryText => queryText.length >= 3),
        debounceTime(500),
        tap(queryText => console.log(queryText))
      );

    queryResult$.subscribe(finalQueryText => {
      let apiResult$ = this._httpClient.get(`http://127.0.0.1:5002/query/${finalQueryText}`);
      apiResult$.subscribe(data => {
        console.log(data);
        this.queryResults = data;
      });  
    })
  }

  articleClicked(articleName: string): any {
    console.log('article clicked!', articleName);
    const articleWithoutSpaces = articleName.replace('%20', ' ');
    let apiResult$ = this._httpClient.get(`http://127.0.0.1:5002/getArticle/${articleName}`);

    apiResult$.subscribe(data => {
      console.log('getArticle response:', data);
    })
  }
}
