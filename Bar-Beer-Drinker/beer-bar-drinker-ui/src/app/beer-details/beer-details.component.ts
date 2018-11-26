import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BeersService, Beer } from '../beers.service';
import { HttpResponse } from '@angular/common/http';

declare const Highcharts: any;

@Component({
  selector: 'app-beer-details',
  templateUrl: './beer-details.component.html',
  styleUrls: ['./beer-details.component.css']
})
export class BeerDetailsComponent implements OnInit {

  beerName: string;
  beerDetails: Beer;

  constructor(
    private beerService: BeersService,
    private route: ActivatedRoute
  ) {
    route.paramMap.subscribe((paramMap) => {

      this.beerName = paramMap.get('beer');

      beerService.getBeer(this.beerName).subscribe(
        data => {
          this.beerDetails = data;
        },
        (error: HttpResponse<any>) => {
          if(error.status === 404){
            alert('Beer not found');
          } else {
            console.error(error.status + ' - ' + error.body);
            alert('An error occurred on the server. ');
          }
        }
      );


      this.beerService.getTopBarsForBeer(this.beerName).subscribe(
        data => {
          console.log(data);
          const bars = [];
          const counts = [];
          data.forEach(bar => {
            bars.push(bar.bar);
            counts.push(bar.quantity);
          });
          this.renderChartBars(bars, counts);
        }
      );

      this.beerService.getTopDrinkersForBeer(this.beerName).subscribe(
        data => {
          console.log(data);
          const drinkers = [];
          const counts = [];
          data.forEach(drinker => {
            drinkers.push(drinker.drinker);
            counts.push(drinker.quantity);
          });
          this.renderChartDrinkers(drinkers, counts);
        }
      );


    });
  }

  ngOnInit() {
  }


  renderChartBars(bars: string[], counts: number[]) {
    Highcharts.chart('bargraph1', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Top bars who sell the most of this beer'
      },
      xAxis: {
        categories: bars,
        title: {
          text: 'Bar'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Quantity Sold'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        beer: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: counts
      }]
    });
  }


  renderChartDrinkers(drinkers: string[], counts: number[]) {
    Highcharts.chart('bargraph2', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Drinkers who buy this beer the most'
      },
      xAxis: {
        categories: drinkers,
        title: {
          text: 'Drinker'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Quantity Consumed'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        beer: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: counts
      }]
    });
  }
}
