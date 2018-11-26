import { Component, OnInit } from '@angular/core';
import { BeersService, Beer} from '../beers.service'

@Component({
  selector: 'app-beers',
  templateUrl: './beers.component.html',
  styleUrls: ['./beers.component.css']
})
export class BeersComponent implements OnInit {

  beers: Beer[];

  constructor(
    public beerService: BeersService
  ) { }

  ngOnInit() {
    this.getBeers();
  }

  getBeers(){
    this.beerService.getBeers().subscribe(
      data => {
        this.beers = data;
      },
      error => {
        alert("Could not find the beer you requested!");
      }
    );
  }

}
