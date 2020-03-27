import { Component, OnInit, Input, Output, EventEmitter } from "@angular/core";
import { faHandPointRight, faTimesCircle } from '@fortawesome/free-solid-svg-icons';
import { ArticleService } from 'src/app/services/article.service';

@Component({
    selector: 'app-selected-article',
    styleUrls: ['./selected-article.component.scss'],
    templateUrl: './selected-article.component.html'
})
export class SelectedArticleComponent implements OnInit {
    @Input() articleName: string;
    articleData: any;

    @Output() removeClicked = new EventEmitter<string>();

    faTimesCircle = faTimesCircle;

    constructor(private _articleService: ArticleService) {}

    ngOnInit(): void {
    }

    articleClicked(articleName: string) {
        this._articleService.openArticleInNewTab(articleName);
    }

    removeArticleClicked(articleName: string) {
        this.removeClicked.emit(articleName);
    }
}
