import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';

@Injectable()
export class ArticleService {
    constructor(private _httpClient: HttpClient) {}

    openArticleInNewTab(articleName: string): any {
        console.log('article clicked!', articleName);
        const apiResult$ = this._httpClient.get(`http://127.0.0.1:5002/getArticle/${articleName}`);

        apiResult$.subscribe((data: any) => {
            console.log('getArticle response:', data);
            window.open(data.url, '_blank');
        });
    }
}
