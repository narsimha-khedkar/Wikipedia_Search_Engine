import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map, tap } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class FileUploadService {
    constructor(private _httpClient: HttpClient) {}

    postFile(fileToUpload: File): Observable<boolean> {
        const endpoint = `http://127.0.0.1:5002/uploadpdf`;
        const formData: FormData = new FormData();
        formData.append('fileKey', fileToUpload, fileToUpload.name);

        return this._httpClient
            .post(endpoint, formData, { headers: {} })
            .pipe(
                tap(streamData => console.log('FileUploadService.postFile API call returned data', streamData)),
                map(() => true),
            );
    }
}
