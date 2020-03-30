import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchPageComponent } from './components/search-page/search-page.component';
import { QueryReportComponent } from './components/query-report/query-report.component';
import { ReactiveFormsModule } from '@angular/forms'
import { HttpClientModule } from '@angular/common/http';
import { FileUploadService } from './services/file-upload.service';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { SelectedArticleComponent } from './components/search-page/components/selected-article/selected-article.component';
import { ArticleService } from './services/article.service';
import { DataSelectionComponent } from './components/search-page/components/data-selection/data-selection.component';


@NgModule({
  declarations: [
    AppComponent,
    SearchPageComponent,
    SelectedArticleComponent,
    QueryReportComponent,
    DataSelectionComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FontAwesomeModule
  ],
  providers: [FileUploadService, ArticleService],
  bootstrap: [AppComponent]
})
export class AppModule { }
