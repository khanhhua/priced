export class Product {
  id: string;
  name: string;
  kind: string;

  pricings: [Price];
}

export class Price {
  id: string;
  effectiveAt: Date;
  expiredDt: Date;
  createdAt: Date;

  value: number;
}

export class Service {
  id: string;
  name: string;
  kind: string;
}

export class Unit {
  id: string;
  name: string;
  shortForm: string;
}

export class Taxcode {
  id: string;
  created_at: Date;
  effected_on: Date;
  expired_on: Date;

  shared: boolean;
  title: string;
  body: string;
}

export class Client {
  id: string;
  client_key: string;
  access_code: string;
}

export class User {
  id: string;
  roles: [String]
}