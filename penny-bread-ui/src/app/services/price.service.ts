import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { appConfig } from "../app.config";

@Injectable({
    providedIn: 'root'
})
export class PriceService {
    private apiUrl = appConfig.apiUrl;

    constructor(private http: HttpClient) {}

    searchProducts(query: string): Observable<any[]> {
        return this.http.get<any[]>(
            `${this.apiUrl}/api/search?q=${query}`
        );
    }
}