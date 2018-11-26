import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface Bar {
 name: string;
 license: string;
 address: string;
 state: string;
 phone: string;
}

@Injectable({
  providedIn: 'root'
})
export class BarsService {

  constructor(
    public http: HttpClient
  ) { }

  getBars() {
    return this.http.get<Bar[]>('/api/bar');
  }
  getBar(bar: string) {
    return this.http.get<Bar>('/api/bar/' + bar);
  }
  getTopDrinkers(bar: string) {
    return this.http.get<any[]>('/api/bar/drinkers/' + bar);
  }
  getTopBeers(bar: string) {
    return this.http.get<any[]>('/api/bar/beers/' + bar);
  }
  getTopManuf(bar: string) {
    return this.http.get<any[]>('/api/bar/manuf/' + bar);
  }

}
