export class Product {
  id: string;
  name: string;
  kind: string;
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
  createdAt: Date;
  effectiveAt: Date;
  expiredAt: Date;

  shared: boolean;
  title: string;
  body: string;

  public static fromJSON(json: any) {
    const taxcode = new Taxcode();
    const {id,
      created_at: createdAt,
      effective_at: effectiveAt,
      expired_at: expiredAt,
      shared,
      title,
      body} = json;

    taxcode.id = id;
    taxcode.createdAt = createdAt
    taxcode.effectiveAt = effectiveAt
    taxcode.expiredAt = expiredAt;
    taxcode.shared = shared;
    taxcode.title = title;
    taxcode.body = body;

    return taxcode;
  }
}

export class Scenario {
  id: string;
  body: string;
}

export class Client {
  id: string;
  clientKey: string;
  accessCode: string;
}

export class User {
  id: string;
  roles: [String]
}